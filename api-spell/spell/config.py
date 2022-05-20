from dynaconf import Dynaconf


settings = Dynaconf(
    envvar_prefix="CEW",
    settings_files=[
        'settings.toml',
        '.secrets.toml',
        '../config/additional_settings.toml'
    ],
    environments=True,
    load_dotenv=True,
    env_switcher="ENV_FOR_TEST",  # to switch environments `export ENV_FOR_DYNACONF=production`
    dotenv_path="../config/.env",  # custom path for .env file to be loaded
    includes=['../config/more_settings.toml']
)

settings.validators.validate()
print("settings is loaded")
