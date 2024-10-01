# Discord Bot

This is a simple Discord bot built using `discord.py` and `python-dotenv` for handling environment variables. The bot listens for specific keywords in messages and responds with corresponding links from a custom `links` module. It also greets new members when they join the server.

## Features
- Responds to keywords in user messages by sending corresponding resources.
- Greets new members when they join the server.
- Basic command: `!hello` which responds with a greeting.
- Uses environment variables for secure token management.

## Requirements

To run this bot, the following Python libraries are required:

- `discord.py==2.3.0`
- `python-dotenv`
- `PyNaCl` (optional, for voice features)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/discord-bot.git
   cd discord-bot

2. Install the required Python libraries:

`pip install -r requirements.txt`

3. Create a .env file in the root directory and add your Discord bot token:

`TOKEN=your-discord-bot-token`

4. Run the bot:

`python main.py`

## Bot Commands

 `!hello`: The bot will respond with "Hello!"

Keyword detection: The bot listens for specific keywords in messages (as defined in the `links.resources` dictionary) and responds with corresponding resources.

## Environment Variables

This bot uses environment variables for security purposes. Create a `.env` file in the root directory and add your bot token:

`TOKEN=your-discord-bot-token`

## Logging

The bot logs its activity in a file named `discord.log`. Logging is configured to output to this file in the following modes:

UTF-8 encoding
Write mode (`w`)

## Custom Modules

`links`: The bot fetches keywords and their corresponding resources from a custom module named `links`. Make sure to populate `links.resources` with the appropriate keywords and their corresponding channel/resource IDs.

## Contributing
Feel free to fork this project, create new features, or fix bugs! Pull requests are welcome.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


### How to Adjust:

- Replace `https://github.com/yourusername/discord-bot.git` with the actual URL of your repository.
- Add any additional features or modules you may implement later.

This `README.md` provides an overview of your bot, installation steps, usage details, and relevant configuration.
