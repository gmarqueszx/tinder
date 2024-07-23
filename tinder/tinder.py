import requests
import time
import json

class Tinder:
    base_url = 'http://127.0.0.1:5000/dados'  # URL da API Flask
    
    def __init__(self, nome, idade, sexo, sexualidade):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo.lower()  # Normalizando para minúsculas
        self.sexualidade = sexualidade.lower()[0]  # Normalizando para minúsculas e pegando a primeira letra

    def __str__(self) -> str:
        return f'Seja bem vindo ao Tinder, {self.nome}!\n'
    
    def procurar_pretendentes(self):
        pretendentes = []
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            usuarios = response.json()

            for usuario in usuarios:
                usuario['sexo'] = usuario['sexo'].lower()
                if usuario['nome'] != self.nome:
                    if self.sexualidade == "h" and usuario['sexo'] != self.sexo:
                        pretendentes.append(usuario)
                    elif self.sexualidade == "g" and usuario['sexo'] == self.sexo:
                        pretendentes.append(usuario)
                    elif self.sexualidade in ["b", "p"]:
                        pretendentes.append(usuario)
        except requests.RequestException as e:
            print(f'Erro ao acessar a API: {e}')
        return pretendentes

    def save_user_data(self):
        user_data = {
            'nome': self.nome,
            'idade': self.idade,
            'sexo': self.sexo,
            'sexualidade': self.sexualidade
        }
        with open(f'{self.nome}.json', 'w') as f:
            json.dump(user_data, f)

    @classmethod
    def load_user_data(cls, nome):
        try:
            with open(f'{nome}.json', 'r') as f:
                user_data = json.load(f)
                return cls(**user_data)
        except FileNotFoundError:
            print('Usuário não encontrado.')
            return None

def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip().lower()
        if valid_options and user_input not in valid_options:
            print(f'Opção inválida. Escolha entre: {", ".join(valid_options)}')
        else:
            return user_input

def main():
    while True:
        print('𝒯𝒾𝓃𝒹𝑒𝓇\n')

        print('1. Faça seu cadastro')
        print('2. Carregar usuário')
        print('3. Sair\n')

        opcao_escolhida = get_user_input('Escolha a opção desejada: ', ['1', '2', '3'])

        if opcao_escolhida == '1':
            print('Ótimo, vamos realizar seu cadastro, preencha os campos abaixo: \n')

            usuario_nome = input('Digite seu nome: ').strip()
            usuario_idade = get_user_input('Digite sua idade: ')
            usuario_sexo = get_user_input('Qual seu sexo (masculino ou feminino)? ', ['masculino', 'feminino'])
            usuario_sexualidade = get_user_input('Qual a sua orientação sexual? (H - Hetero, G - Homo, B - Bissexual, P - Pansexual) ', ['h', 'g', 'b', 'p'])
            
            usuario = Tinder(usuario_nome, usuario_idade, usuario_sexo, usuario_sexualidade)
            print(usuario)
            usuario.save_user_data()

        elif opcao_escolhida == '2':
            nome = input('Digite o nome do usuário para carregar: ').strip()
            usuario = Tinder.load_user_data(nome)
            if usuario:
                print(usuario)
            else:
                continue

        elif opcao_escolhida == '3':
            print('Finalizando programa...')
            time.sleep(2)
            break

        else:
            input('Erro, digite qualquer tecla para voltar ao menu: \n')

        if usuario:
            while True:
                print('𝒯𝒾𝓃𝒹𝑒𝓇\n')

                print('1. Visualizar dados cadastrados')
                print('2. Adicionar ou editar biografia')
                print('3. Procurar pretendentes')
                print('4. Sair')

                opcao_escolhida2 = get_user_input('Escolha a opção desejada: \n', ['1', '2', '3', '4'])

                if opcao_escolhida2 == '1':
                    print(f'Nome: {usuario.nome} | Idade: {usuario.idade} | Sexo: {usuario.sexo} | Orientação Sexual: {usuario.sexualidade}')
                    time.sleep(2)
                elif opcao_escolhida2 == '2':
                    biografia = input('Fale um pouco sobre você: ')
                    print(f'Biografia: {biografia}')
                elif opcao_escolhida2 == '3':
                    pretendentes = usuario.procurar_pretendentes()
                    if pretendentes:
                        print("Pretendentes encontrados:")
                        for p in pretendentes:
                            print(f'Nome: {p["nome"]} | Idade: {p["idade"]} | Sexo: {p["sexo"]} | Orientação Sexual: {p["sexualidade"]}')
                    else:
                        print("Nenhum pretendente encontrado.")
                    time.sleep(2)
                elif opcao_escolhida2 == '4':
                    print('Finalizando programa...')
                    time.sleep(2)
                    break
                else:
                    input('Erro, digite qualquer tecla para voltar ao menu: \n')

if __name__ == "__main__":
    main()