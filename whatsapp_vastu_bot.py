from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
Collecting flask
  Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting openai
  Downloading openai-1.61.0-py3-none-any.whl.metadata (27 kB)
Collecting twilio
  Downloading twilio-9.4.4-py2.py3-none-any.whl.metadata (12 kB)
Collecting Werkzeug>=3.1 (from flask)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2 (from flask)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from flask)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting anyio<5,>=3.5.0 (from openai)
  Downloading anyio-4.8.0-py3-none-any.whl.metadata (4.6 kB)
Collecting distro<2,>=1.7.0 (from openai)
  Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting httpx<1,>=0.23.0 (from openai)
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting jiter<1,>=0.4.0 (from openai)
  Downloading jiter-0.8.2-cp313-cp313-win_amd64.whl.metadata (5.3 kB)
Collecting pydantic<3,>=1.9.0 (from openai)
  Downloading pydantic-2.10.6-py3-none-any.whl.metadata (30 kB)
Collecting sniffio (from openai)
  Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tqdm>4 (from openai)
  Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-extensions<5,>=4.11 (from openai)
  Downloading typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
Collecting requests>=2.0.0 (from twilio)
  Downloading requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting PyJWT<3.0.0,>=2.0.0 (from twilio)
  Downloading PyJWT-2.10.1-py3-none-any.whl.metadata (4.0 kB)
Collecting aiohttp>=3.8.4 (from twilio)
  Downloading aiohttp-3.11.11-cp313-cp313-win_amd64.whl.metadata (8.0 kB)
Collecting aiohttp-retry>=2.8.3 (from twilio)
  Downloading aiohttp_retry-2.9.1-py3-none-any.whl.metadata (8.8 kB)
Collecting aiohappyeyeballs>=2.3.0 (from aiohttp>=3.8.4->twilio)
  Downloading aiohappyeyeballs-2.4.4-py3-none-any.whl.metadata (6.1 kB)
Collecting aiosignal>=1.1.2 (from aiohttp>=3.8.4->twilio)
  Downloading aiosignal-1.3.2-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.8.4->twilio)
  Downloading attrs-25.1.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.8.4->twilio)
  Downloading frozenlist-1.5.0-cp313-cp313-win_amd64.whl.metadata (14 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.8.4->twilio)
  Downloading multidict-6.1.0-cp313-cp313-win_amd64.whl.metadata (5.1 kB)
Collecting propcache>=0.2.0 (from aiohttp>=3.8.4->twilio)
  Downloading propcache-0.2.1-cp313-cp313-win_amd64.whl.metadata (9.5 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.8.4->twilio)
  Downloading yarl-1.18.3-cp313-cp313-win_amd64.whl.metadata (71 kB)
Collecting idna>=2.8 (from anyio<5,>=3.5.0->openai)
  Downloading idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting colorama (from click>=8.1.3->flask)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting certifi (from httpx<1,>=0.23.0->openai)
  Downloading certifi-2025.1.31-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai)
  Downloading httpcore-1.0.7-py3-none-any.whl.metadata (21 kB)
Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx<1,>=0.23.0->openai)
  Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Using cached MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl.metadata (4.1 kB)
Collecting annotated-types>=0.6.0 (from pydantic<3,>=1.9.0->openai)
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.27.2 (from pydantic<3,>=1.9.0->openai)
  Downloading pydantic_core-2.27.2-cp313-cp313-win_amd64.whl.metadata (6.7 kB)
Collecting charset-normalizer<4,>=2 (from requests>=2.0.0->twilio)
  Downloading charset_normalizer-3.4.1-cp313-cp313-win_amd64.whl.metadata (36 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.0.0->twilio)
  Downloading urllib3-2.3.0-py3-none-any.whl.metadata (6.5 kB)
Using cached flask-3.1.0-py3-none-any.whl (102 kB)
Downloading openai-1.61.0-py3-none-any.whl (460 kB)
Downloading twilio-9.4.4-py2.py3-none-any.whl (1.9 MB)
 1.9/1.9 MB 12.9 MB/s eta 0:00:00
Downloading aiohttp-3.11.11-cp313-cp313-win_amd64.whl (436 kB)
Downloading aiohttp_retry-2.9.1-py3-none-any.whl (10.0 kB)
Downloading anyio-4.8.0-py3-none-any.whl (96 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Downloading distro-1.9.0-py3-none-any.whl (20 kB)
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.7-py3-none-any.whl (78 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
Downloading jiter-0.8.2-cp313-cp313-win_amd64.whl (203 kB)
Downloading pydantic-2.10.6-py3-none-any.whl (431 kB)
Downloading pydantic_core-2.27.2-cp313-cp313-win_amd64.whl (2.0 MB)
2.0/2.0 MB 25.7 MB/s eta 0:00:00
Downloading PyJWT-2.10.1-py3-none-any.whl (22 kB)
Downloading requests-2.32.3-py3-none-any.whl (64 kB)
Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)
Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
Downloading typing_extensions-4.12.2-py3-none-any.whl (37 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading aiohappyeyeballs-2.4.4-py3-none-any.whl (14 kB)
Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading attrs-25.1.0-py3-none-any.whl (63 kB)
Downloading certifi-2025.1.31-py3-none-any.whl (166 kB)
Downloading charset_normalizer-3.4.1-cp313-cp313-win_amd64.whl (102 kB)
Downloading frozenlist-1.5.0-cp313-cp313-win_amd64.whl (51 kB)
Downloading idna-3.10-py3-none-any.whl (70 kB)
Using cached MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl (15 kB)
Downloading multidict-6.1.0-cp313-cp313-win_amd64.whl (28 kB)
Downloading propcache-0.2.1-cp313-cp313-win_amd64.whl (43 kB)
Downloading urllib3-2.3.0-py3-none-any.whl (128 kB)
Downloading yarl-1.18.3-cp313-cp313-win_amd64.whl (315 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading h11-0.14.0-py3-none-any.whl (58 kB)
Installing collected packages: urllib3, typing-extensions, sniffio, PyJWT, propcache, multidict, MarkupSafe, jiter, itsdangerous, idna, h11, frozenlist, distro, colorama, charset-normalizer, certifi, blinker, attrs, annotated-types, aiohappyeyeballs, yarl, Werkzeug, tqdm, requests, pydantic-core, Jinja2, httpcore, click, anyio, aiosignal, pydantic, httpx, flask, aiohttp, openai, aiohttp-retry, twilio
Successfully installed Jinja2-3.1.5 MarkupSafe-3.0.2 PyJWT-2.10.1 Werkzeug-3.1.3 aiohappyeyeballs-2.4.4 aiohttp-3.11.11 aiohttp-retry-2.9.1 aiosignal-1.3.2 annotated-types-0.7.0 anyio-4.8.0 attrs-25.1.0 blinker-1.9.0 certifi-2025.1.31 charset-normalizer-3.4.1 click-8.1.8 colorama-0.4.6 distro-1.9.0 flask-3.1.0 frozenlist-1.5.0 h11-0.14.0 httpcore-1.0.7 httpx-0.28.1 idna-3.10 itsdangerous-2.2.0 jiter-0.8.2 multidict-6.1.0 openai-1.61.0 propcache-0.2.1 pydantic-2.10.6 pydantic-core-2.27.2 requests-2.32.3 sniffio-1.3.1 tqdm-4.67.1 twilio-9.4.4 typing-extensions-4.12.2 urllib3-2.3.0 yarl-1.18.3 if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)
