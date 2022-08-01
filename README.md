# Docker aiogram bot
Telegram bot translitetare full name from cyrillic to latin to the norm of MFA.

How to run:
- add TOKEN from @BotFather to dockerfile

```
docker build -t tdtranslit .
docker run -d -p 80:80 tgtranslit
```
