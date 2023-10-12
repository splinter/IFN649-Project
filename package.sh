mkdir bin
cp -r platform bin
cp -r shared bin
mkdir bin/plant_register
cp -r bin/platform/lambdas/table_clients bin/plant_register/table_clients
cp  bin/platform/lambdas/plant_register/lambda_function.py bin/plant_register


mkdir bin/command_register
mkdir bin/command_register/table_clients
cp -r platform/lambdas/table_clients/* bin/command_register/table_clients
cp -r platform/lambdas/commands_register/* bin/command_register


mkdir bin/commands_list
mkdir bin/commands_list/table_clients
cp -r platform/lambdas/table_clients/* bin/commands_list/table_clients
cp -r platform/lambdas/command_list/* bin/commands_list


mkdir bin/command_update
mkdir bin/command_update/table_clients
cp -r platform/lambdas/table_clients/* bin/command_update/table_clients
cp -r platform/lambdas/command_update/* bin/command_update