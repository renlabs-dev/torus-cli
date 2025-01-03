# Torus CLI

The Torus CLI serves as an official SDK for the network, offering a streamlined and
user-friendly experience. It is designed for simplicity and scalable
development. To learn more [visit docs](https://docs.torus.network/installation/setup-torus-cli)

## Contents

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Discord Chat](https://img.shields.io/badge/discord-join%20chat-blue.svg)](https://discord.gg/W2H8Q6aE)
[![PyPI version](https://badge.fury.io/py/torus.svg)](https://pypi.org/project/torus/)

- [Torus CLI](#torus-cli)
  - [Contents](#contents)
  - [Installation with `pip`](#installation-with-pip)
  - [Installation with Nix](#installation-with-nix)
  - [Features](#features)
  - [CLI Usage](#cli-usage)
  - [Examples](#examples)
    - [Retrieving Balance](#retrieving-balance)
    - [Creating a Key](#creating-a-key)
    - [Retrieving Key Info](#retrieving-key-info)
    - [Listing Keys](#listing-keys)
    - [List Keys With Balances](#list-keys-with-balances)
    - [Retrieving Agent Information](#retrieving-agent-information)
    - [Retrieving Global Parameters](#retrieving-global-parameters)
    - [Retrieving Circulating Supply](#retrieving-circulating-supply)
  - [Completions](#completions)
  - [Contributing](#contributing)

## Installation with `pip`

Requirements: Python 3.10+

Install the `torus-cli` Python package directly with `pip`:

```sh
pip install torus
```

Or add it to your Poetry project with:

```sh
poetry add torus
```

## Installation with Nix

To install `torus` the torus cli with Nix
```sh
nix profile install .
```

## Features

The `torus-cli` offers a variety of features for token management and agent interaction:

- Commands for managing keys, tokens, and agents
- Key management including creation and listing
- Token operations such as transferring and staking
- Agent management for registration, curation and updates
- Participation in governance processes


## CLI Usage

The CLI commands are structured as follows:

```sh
torus-cli [OPTIONS] COMMAND [ARGS]
```

There are six top-level subcommands:

- **balance**: Manage token balances and staking.
- **key**: Handle key creation and management.
- **agent**: Manage information and operations related to agents.
- **network**: Interact with network operations like block and proposal management.
- **misc**: Access miscellaneous information such as APR and circulating supply.

```sh
torus-cli subcommand [OPTIONS] COMMAND [ARGS]...
```

## Examples

### Retrieving Balance

```sh
# Show staked, free and total balance.
torus-cli balance show 5FgfC2DY4yreEWEughz46RZYQ8oBhHVqD9fVq6gV89E6z4Ea
```

### Creating a Key

```sh
torus-cli key create key_name
```

### Retrieving Key Info

```sh
torus-cli key show key_name

# Add the `--show-private` flag to show sensitive fields like private key.
torus-cli key show key_name --show-private
```

### Listing Keys

```sh
# Lists the names and addresses of keys stored on disk.
torus-cli key list
```

### List Keys With Balances

```sh
# Lists keys stored on disk with their balance (free, staked and total).
torus-cli key balances
```

### Retrieving Agent Information

```sh
# Note that the agent has to be registered on the network.
torus-cli agent info vali::calc [--balance]
```

### Retrieving Global Parameters

```sh
torus-cli network params
```

### Retrieving Circulating Supply

```sh
# Gets all tokens then were ever emitted minus burned tokens.
torus-cli misc circulating-supply
```

## Completions

You can enable completions for your shell by running:

```sh
# On bash
torus-cli --install-completion bash
# On zsh
torus-cli --install-completion zsh
```

## Contributing

Bug reports and pull requests and other forms of contribution are welcomed and
encouraged! :)

To report a bug or request a feature, please [open an issue on GitHub].

If you have any questions, feel free to ask on the [CLI Discord channel] or
post on our [GitHub discussions page].

To contribute to the codebase, using Poetry you can install the development dependencies with:

```sh
poetry install --with dev
```

it can [require some environment-specific binaries to be installed][ruff-installation]

---

[open an issue on GitHub]: https://github.com/renlabs-dev/torus-cli/issues/new/choose
[torus-cli Discord channel]: https://go.renlabs-dev.org/torus-cli-channel
[GitHub discussions page]: https://github.com/renlabs-dev/torus-cli/discussions
[ruff-installation]: https://docs.astral.sh/ruff/installation/
