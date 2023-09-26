mkdir bin
cp -r platform bin
cp -r shared bin
mkdir bin/plant_register
cp -r bin/platform/lambdas/table_clients bin/plant_register/table_clients
cp  bin/platform/lambdas/plant_register/lambda_function.py bin/plant_register