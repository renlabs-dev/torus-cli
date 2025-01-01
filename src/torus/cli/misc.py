import typer
from typer import Context

from torus._common import BalanceUnit, format_balance
from torus.balance import from_nano
from torus.cli._common import make_custom_context, print_module_info
from torus.client import TorusClient
from torus.compat.key import local_key_addresses
from torus.misc import get_map_modules

misc_app = typer.Typer(no_args_is_help=True)


def circulating_tokens(c_client: TorusClient) -> int:
    """
    Gets total circulating supply
    """

    with c_client.get_conn(init=True) as substrate:
        block_hash = substrate.get_block_hash()

    total_balance = c_client.get_total_free_issuance(block_hash=block_hash)
    total_stake = c_client.get_total_stake(block_hash=block_hash)
    return total_stake + total_balance


@misc_app.command()
def circulating_supply(ctx: Context, unit: BalanceUnit = BalanceUnit.joule):
    """
    Gets the value of all keys on the network, stake + balances
    """
    context = make_custom_context(ctx)
    client = context.com_client()

    with context.progress_status(
        "Getting circulating supply, across all subnets..."
    ):
        supply = circulating_tokens(client)

    context.output(format_balance(supply, unit))


@misc_app.command()
def apr(ctx: Context, fee: int = 0):
    """
    Gets the current staking APR on validators.
    The miner reinvest rate & fee are specified in percentages.
    """
    context = make_custom_context(ctx)
    client = context.com_client()

    # adjusting the fee to the correct format
    # the default validator fee on the commune network is 20%
    fee_to_float = fee / 100

    # network parameters
    block_time = 8  # seconds
    seconds_in_a_day = 86400
    blocks_in_a_day = seconds_in_a_day / block_time

    with context.progress_status("Getting staking APR..."):
        unit_emission = client.get_unit_emission()
        total_staked_tokens = client.query("TotalStake")
    # 50% of the total emission goes to stakers
    daily_token_rewards = blocks_in_a_day * from_nano(unit_emission) / 2
    _apr = (
        (daily_token_rewards * (1 - fee_to_float) * 365)
        / total_staked_tokens
        * 100
    )

    context.output(f"Fee {fee} | APR {_apr:.2f}%")


@misc_app.command(name="stats")
def stats(ctx: Context, balances: bool = False, netuid: int = 0):
    context = make_custom_context(ctx)
    client = context.com_client()

    with context.progress_status(
        f"Getting Modules on a subnet with netuid {netuid}..."
    ):
        modules = get_map_modules(client, include_balances=balances)
    modules_to_list = [value for _, value in modules.items()]
    local_keys = local_key_addresses(password_provider=context.password_manager)
    local_modules = [
        *filter(
            lambda module: module["key"] in local_keys.values(), modules_to_list
        )
    ]

    print_module_info(client, local_modules, context.console, netuid, "agents")


@misc_app.command(name="treasury-address")
def get_treasury_address(ctx: Context):
    context = make_custom_context(ctx)
    client = context.com_client()

    with context.progress_status("Getting DAO treasury address..."):
        dao_address = client.get_dao_treasury_address()
    context.output(dao_address)
