from envyaml import EnvYAML

config_example = EnvYAML('config/examples.yml')
print(config_example['token'])
