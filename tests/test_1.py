from src import config

# Duas referências obtidas para a configuração representam o mesmo objeto
config1 = AppConfig()
config2 = AppConfig()
print(config1 is config2) 

# Uma alteração realizada em uma referência pode ser observada pela outra
config1.environment = 'development'
print(config2.environment == 'development')

# Os valores alterados não são restaurados quando a configuração é obtida novamente
config3 = AppConfig()
print(config3.environment == 'development')