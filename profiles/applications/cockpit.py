import archinstall

# Define the package list in order for lib to source
# which packages will be installed by this profile
__packages__ = ["cockpit", "udisks2", "packagekit"]

archinstall.storage['installation_session'].add_additional_packages(__packages__)

archinstall.storage['installation_session'].enable_service('cockpit.socket')
