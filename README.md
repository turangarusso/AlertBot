# AlertBot
A simple discord bot that send an alert when a user login in windows server

<h1 align="center">
  <br>





     _____    __   ______   ______   ______   ______   _____      
    /\  __-. /\ \ /\  ___\ /\  ___\ /\  __ \ /\  == \ /\  __-.   
    \ \ \/\ \\ \ \\ \___  \\ \ \____\ \ \/\ \\ \  __< \ \ \/\ \  
     \ \____- \ \_\\/\_____\\ \_____\\ \_____\\ \_\ \_\\ \____-   
      \/____/  \/_/ \/_____/ \/_____/ \/_____/ \/_/ /_/ \/____/    
                                                                                         
                                   
                                  
                                  
                                  
                                  
                           
  <br>
 AlertBot
  <br>
</h1>

<h4 align="center">A simple discord bot that send an alert when a user login in windows server
.</h4>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://www.trendingus.com/wp-content/uploads/2021/09/Trending-Discord-Bots-to-Game-Up-Your-Server-1920x768.jpg)

## Key Features

* Send custom message on a discord server channel
* Ghost process. 
* You can use it to configure login alert on Windows/Linux VPS.


## How To Use

You can build the project using Pycharm, then you need to insert your discord bot token inside the code

```
client = commands.Bot(command_prefix=("t!"))
token = "Your Discord Developer Token"

```

Change the discord channel ID 

```
async def on_ready():
    print(client.user, client.user.id)
    channel = client.get_channel(968628680559575043) <-- your discord channel ID

```
Change the message text if you want

```

await channel.send('Un utente è nella vps, non entrarci')

```

Host the boot on a server!

> **Note**
> You need to setup your windows server, create a task that will start the bot when a user login


## Credits

Russo Giovanni M.


## License

MIT

---

