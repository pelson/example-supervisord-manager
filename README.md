This repository is a proof-of-concept implementation of a git repository being the canonical source for the definition of daemon processes (using supervisor configs).

In practice a simple webhook would be set up to listen on the desired git repository, and the listening service would then run the update script.


## Note

Whilst this repository does update the *daemons* whenever the config changes, it does not necessarily know if the underlying *application* has changed.
Some further work is needed to be able to identify whether the existing daemon should be restarted in that situation.
