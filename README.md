# evlampiy_notes_bot

[![CI](https://github.com/YastYa/evlampiy_notes_tgbot/actions/workflows/deploy.yml/badge.svg)](https://github.com/YastYa/evlampiy_notes_tgbot/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

https://t.me/evlampiy_notes_bot

Telegram bot for managing notes with voice-to-text translation.

## Features

- Translate voice messages to text (supports English, German, Russian, Spanish)
- Custom language settings per chat/user
- GPT command integration via voice
- Export notes to Obsidian via GitHub

## Requirements

- Python 3.12+
- MongoDB
- FFmpeg
- [Wit.ai](https://wit.ai/) tokens for speech recognition
- Telegram Bot token

### [Installation, configuration and deploy](DEPLOY.md)

### Bot commands

- `/start` — Show help and current settings
- `/choose_your_language` — Set voice recognition language

## Roadmap

- [x] Voice-to-text translation
- [x] Multi-language support
- [ ] GPT command integration
- [ ] Export to Obsidian
- [ ] Message classification by topics
- [ ] ChatMemberUpdated handler for cleanup

## License

[GPL-3.0](LICENSE)
