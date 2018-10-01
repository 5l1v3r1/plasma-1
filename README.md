# PLASMA

Plasma is a command-line intelligence gathering tool inspired by Black Hills' Recon-NG.

The tool is integrated to multiple intel sources and fetches data from them. We tried our best to come up with solutions within the tool for rate limits.

If you do not want any module you can just remove it from there. You can also add your own modules for intel gathering.

The tool currently supports only python3 and causes issues on windows due to color scheme.

# Adding New Modules

Any new module can be added to Plasma. Create a python3 module, place it in ./modules and just call it from the main menu.

*Note: It would be really nice if you keep the config files for modules and the main menu separate although they are same.

# Modules

1) ip-api                       Gather intel on any ip.
2) pipl                         Run a search on a person, find their public profiles.
3) opencorporates               Run a search on companies, oficers that work in them. Quickly find                                                             connections between companies and the people the work in them.

More modules will be added soon.

Keep Calm and Gather Intel.
