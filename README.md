# Buffs

1) Ensure logging is turned on on the character you wish to be your buffer  (ie:  /log )
2) Change the PATH_TO_LOG  and LOG_NAME to match the location and name of your logfile.
3) Add lines to BUFFINFO as needed.  The general format is

triggertext = gemslot, totalcasttime

For example:  
conviction = 5,10

- Your character would cast whatever spell is in gem slot #5 when someone sends you a tell with the single word: conviction.  Ideally the triggertext would be meaningful (eg: the spell in slot 5 is actually Conviction)

- It will allow 10 seconds before trying to cast any other buffs.  In general your cast time should be about 3 seconds longer than the cast time of your spell  (to account for spell cooldown and lag). If this time is too short you may miss buff requests

