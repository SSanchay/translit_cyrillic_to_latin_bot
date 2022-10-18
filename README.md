# Docker aiogram bot
Telegram bot translitetare full name from cyrillic to latin to the norm of MFA.

 <img src="https://user-images.githubusercontent.com/40661291/196414705-688418aa-7553-47b7-b516-dd8446221afe.png"/>

How to run:
- add TOKEN from @BotFather to dockerfile

```
docker build -t tgtranslit .
docker run -d -p 80:80 tgtranslit
```
