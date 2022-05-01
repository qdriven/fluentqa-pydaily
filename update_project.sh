#!/usr/bin/env sh
PACKAGE_NAME=$1
#mv src/prpro_template src/${PACKAGE_NAME}

sed -i "" "s/pypro-templates/${PACKAGE_NAME}/g" pyproject.toml
sed -i "" "s/pypro_templates/${PACKAGE_NAME}/g" pyproject.toml

echo "check setting...."
poetry install
poetry build
pytest