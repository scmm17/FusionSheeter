# Importing sample Fusion Command
# Could import multiple Command definitions here
from .FusionSheeterCommand import FusionSheeterSizeCommand, FusionSheeterCreateCommand, \
     FusionSheeterBuildCommand, FusionSheeterSyncCommand, FusionSheeterOpenSheetCommand,\
     FusionSheeterFeaturePullCommand, FusionSheeterBOMPullCommand, FusionSheeterBOMPushCommand, \
    FusionSheeterParameterPullCommand

commands = []
command_definitions = []

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Sync With Google Sheet',
    'cmd_description': 'Synchronize Design Parameters, BOM Data and Feature Suppression with a Google Sheet',
    'cmd_id': 'cmdID_FusionSheeterSyncCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Sheeter',
    'command_promoted': True,
    'class': FusionSheeterSyncCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Link Design to Google Sheet',
    'cmd_description': 'Creates a new Google Sheets Document in your Google Drive based on the current active model.  '
                       'Establishes a link from the current design to the new spreadsheet.',
    'cmd_id': 'cmdID_FusionSheeterCreateCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Sheeter',
    'command_promoted': False,
    'class': FusionSheeterCreateCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Open Sheet',
    'cmd_description': 'Open Sheet Associated with this Fusion 360 Design',
    'cmd_id': 'cmdID_FusionSheeterOpenSheetCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Sheeter',
    'command_promoted': False,
    'class': FusionSheeterOpenSheetCommand
}
command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Change Size',
    'cmd_description': 'Change association of active model to a different row in Sheets Document',
    'cmd_id': 'cmdID_FusionSheeterCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Sheeter',
    'class': FusionSheeterSizeCommand
}
command_definitions.append(cmd)

# # Define parameters for 1st command
# cmd = {
#     'cmd_name': 'Pull BOM Data',
#     'cmd_description': 'Update Fusion 360 Component Meta-Data from Google Sheets',
#     'cmd_id': 'cmdID_FusionSheeterBOMPullCommand',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Sheeter',
#     'command_promoted': False,
#     'class': FusionSheeterBOMPullCommand
# }
# command_definitions.append(cmd)
#
# # Define parameters for 1st command
# cmd = {
#     'cmd_name': 'Pull Parameter Data',
#     'cmd_description': 'Update Fusion 360 Component Parameters from Google Sheets',
#     'cmd_id': 'cmdID_FusionSheeterParametersPullCommand',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Sheeter',
#     'command_promoted': False,
#     'class': FusionSheeterParameterPullCommand
# }
# command_definitions.append(cmd)
#
# # Define parameters for 1st command
# cmd = {
#     'cmd_name': 'Pull Feature Data',
#     'cmd_description': 'Update Fusion 360 Feature Suppression from Google Sheets',
#     'cmd_id': 'cmdID_FusionSheeterFeaturePullCommand',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Sheeter',
#     'command_promoted': False,
#     'class': FusionSheeterFeaturePullCommand
# }
# command_definitions.append(cmd)
#
# # Define parameters for 1st command
# cmd = {
#     'cmd_name': 'Push BOM Data',
#     'cmd_description': 'Update Google Sheets Document with Fusion 360 Component Meta-Data',
#     'cmd_id': 'cmdID_FusionSheeterBOMPushCommand',
#     'cmd_resources': './resources',
#     'workspace': 'FusionSolidEnvironment',
#     'toolbar_panel_id': 'Sheeter',
#     'command_promoted': False,
#     'class': FusionSheeterBOMPushCommand
# }
# command_definitions.append(cmd)

# Define parameters for 1st command
cmd = {
    'cmd_name': 'Build All Sizes',
    'cmd_description': 'Create Unique Component for each row in Google Sheet Document',
    'cmd_id': 'cmdID_FusionSheeterBuildCommand',
    'cmd_resources': './resources',
    'workspace': 'FusionSolidEnvironment',
    'toolbar_panel_id': 'Sheeter',
    'command_promoted': False,
    'class': FusionSheeterBuildCommand
}
command_definitions.append(cmd)

# Set to True to display various useful messages when debugging your app
debug = False


# Don't change anything below here:
for cmd_def in command_definitions:
    command = cmd_def['class'](cmd_def, debug)
    commands.append(command)


def run(context):
    for run_command in commands:
        run_command.on_run()


def stop(context):
    for stop_command in commands:
        stop_command.on_stop()
