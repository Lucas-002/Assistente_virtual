# Assistente Virtual com PLN

Este projeto consiste em um sistema de assistência virtual desenvolvido utilizando técnicas de Processamento de Linguagem Natural (PLN). O sistema integra módulos de conversão de texto para áudio (TTS) e de fala para texto (STT), possibilitando a interação por comandos de voz.

## Funcionalidades

- **Text-to-Speech (TTS):** Converte textos em áudio usando a biblioteca [gTTS](https://github.com/pndurette/gTTS).
- **Speech-to-Text (STT):** Converte a fala do usuário em texto por meio da biblioteca [SpeechRecognition](https://github.com/Uberi/speech_recognition).
- **Automação por comandos de voz:**  
  - Pesquisa vídeos no YouTube.  
  - Consulta a Wikipedia e lê um resumo da pesquisa.  
  - Conta piadas utilizando a biblioteca [pyjokes](https://pypi.org/project/pyjokes/).  
  - Informa a hora atual.  
  - Abre o Google Maps para localizar farmácias próximas.  
  - Encerra a execução do programa mediante comando.

## Requisitos

- **Python 3.x**

### Bibliotecas Necessárias

- `speech_recognition`
- `gTTS`
- `playsound`
- `wikipedia`
- `pyjokes`
- Outras bibliotecas padrão: `os`, `datetime`, `webbrowser`

Para instalar as bibliotecas, utilize o `pip`:

```bash
pip install SpeechRecognition gTTS playsound wikipedia pyjokes
```

**Observação:**  
Para o funcionamento do módulo de reconhecimento de fala, pode ser necessário instalar o `pyaudio`. Em sistemas Windows, você pode utilizar:

```bash
pip install pyaudio
```

Em outros sistemas, consulte a documentação do [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/).

## Como Usar

1. **Verifique o Microfone:** Certifique-se de que seu microfone está configurado e funcionando corretamente.
2. **Execute o Script:**  
   No terminal, execute o arquivo Python do projeto:

   ```bash
   python nome_do_arquivo.py
   ```

3. **Interaja com o Assistente:**  
   O sistema ficará em modo de escuta contínua e aguardará seus comandos. Exemplos de comandos:
   - **YouTube:** Diga "youtube" e, em seguida, informe o termo de pesquisa para abrir os resultados no navegador.
   - **Wikipedia:** Diga "wikipedia" e informe o termo desejado para receber um resumo.
   - **Piada:** Diga "piada" para ouvir uma piada.
   - **Horas:** Diga "horas" para que o assistente informe a hora atual.
   - **Farmácia:** Diga "farmácia" para abrir o Google Maps com uma busca por farmácias próximas.
   - **Sair:** Diga "sair" para encerrar o programa.

## Estrutura do Código

- **`get_audio()`:**  
  Captura áudio do microfone e converte a fala em texto utilizando a API do Google.
  
- **`speak(text)`:**  
  Converte o texto em áudio por meio da gTTS, salva o áudio temporariamente e o reproduz com a biblioteca `playsound`.
  
- **`respond(command)`:**  
  Analisa o comando de voz reconhecido e executa a ação correspondente (abrir links, pesquisar na Wikipedia, contar piadas, etc.).
  
- **Loop Principal:**  
  O programa permanece em execução, ouvindo e respondendo aos comandos do usuário em tempo real.

## Referências

- [Text-to-Speech Example](https://github.com/diegobrunoDIO/Text-to-Speech-DIO)
- [Speech-to-Text Example](https://github.com/diegobrunoDIO/Speech-to-text-ML-DIO)
- Slides e materiais do curso utilizados durante as aulas.
