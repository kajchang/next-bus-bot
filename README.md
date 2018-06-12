# Next Bus Bot (WIP)

Discord Bot that lets users schedule notifications with bus times from the [NextBus API](https://gist.github.com/grantland/7cf4097dd9cdf0dfed14). Discord Bot uses MongoDB to manage the scheduled notifications.

The bot works for any bus system that uses NextBus to provide time predictions. You can add the bot to your server [here](https://discordapp.com/oauth2/authorize?client_id=454489707360026626&scope=bot). 

The bot might be on and off while I take it down to add features and test.

## Commands

The bot currently only takes commands (except for !bus info) in private messages. The bot's prefix is '!bus '.

### !bus start
The bot will give you basic information on itself and it's commands.

### !bus add
The bot will give you prompts to configure a notification.

### !bus list
The bot will list all current notifications with corresponding IDs for use when calling /delete.

### !bus delete|d|D id
The bot will delete the specified notification.

### !bus change|c|C action id
The bot will give you prompts to edit the stop and line of the given notification.

To edit time, the action parameter should be time or t.

To edit stop, the action parameter should be stop or s.

### !bus info
The bot will provide the number of servers it is a part of and its invite link.

# TODO

- Ability to set notifications to weekdays only

- Improve readability

- Add some general features
