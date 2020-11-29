# Chat

## Features
- Allow registered users to log in and talk with other users in a chatroom.
- Allow users to post messages as commands into the chatroom with the following format
/stock=stock_code
- Bot that will call an API using the stock_code as a parameter
(https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv, here aapl.us is the
stock_code)
- The bot parse the received CSV file and then it should send a message back into
the chatroom using a message broker (huey). The message will be a stock quote
using the following format: “AAPL.US quote is $93.42 per share”. The post owner will be
the bot.
- Chat messages ordered by their timestamps and show only the last 50
messages.
- Unit test the functionality you prefer.

## Run api local (backend) 

1.  How do I get set up this api? Install python +3.7 and create a virtualenv using virtualenv.

2.  Create and running a virtualenv
    ```
    user@server:~$ source venv/bin/activate
    ```
3.  Running tests 
    ```
    user@server:~$ pytest -v
    ```
4. Running api App:
    ```
    (ensembl-api-env) user@server:~$ gunicorn app:app -b localhost:8881
    ```
    
    The api will be available on http://127.0.0.1:8000/api/v1/health
    
    A GET request example
    
    ``` 
    curl --location --request GET 'http://127.0.0.1:8881/api/v1/chat/messages'
    ```

    Response example:
    
   ```
   {
    "results": [
        {
            "id": "2Cty2VC2xaLgWJLGaTMl",
            "message": "Oiee",
            "sender": {
                "uid": "oOaHPwczePZ8PuIRtnLHeUE3pcD3",
                "created_at": "2020-10-31T02:29:06.040000+00:00",
                "last_login_at": "2020-10-31T02:29:06.040000+00:00",
                "identifier": "dedeco@gmail.com",
                "id": "hJkqKYphnlt03e59AxVa",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:16:29.909150+00:00"
        },
        {
            "id": "Knz1qZzND2dJAumys2bW",
            "message": "dsds /stock=amzn.us",
            "sender": {
                "uid": "oOaHPwczePZ8PuIRtnLHeUE3pcD3",
                "created_at": "2020-10-31T02:29:06.040000+00:00",
                "last_login_at": "2020-10-31T02:29:06.040000+00:00",
                "identifier": "dedeco@gmail.com",
                "id": "hJkqKYphnlt03e59AxVa",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:16:36.486053+00:00"
        },
        {
            "id": "zZ8j9Hs2KFJCVLzqCzFP",
            "message": "amzn.us quote is $3004.48 (close) per share",
            "sender": {
                "uid": "WhmylOoKgsT4zM8nKsJLTcnyA0v1",
                "created_at": "2020-11-02T22:34:55.684000+00:00",
                "last_login_at": "2020-11-02T22:34:55.684000+00:00",
                "identifier": "chatbot@chat.com",
                "id": "gv2wd0CevtWHSL6hpLpQ",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:16:37.788566+00:00"
        },
        {
            "id": "ttT2Vq0YtLGljoQtfwW9",
            "message": "Hi",
            "sender": {
                "uid": "8IHMRHXQ1vOlRfnYE709G2vU3R12",
                "created_at": "2020-11-02T18:10:55.877000+00:00",
                "last_login_at": "2020-11-02T18:10:55.877000+00:00",
                "identifier": "dedecu@hotmail.com",
                "id": "Ilq4ep1uzVYyRTGrmrYx",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:16:50.482897+00:00"
        },
        {
            "id": "HQ6SJMIqv4bZOXZgaduR",
            "message": "/stock=appl.us",
            "sender": {
                "uid": "8IHMRHXQ1vOlRfnYE709G2vU3R12",
                "created_at": "2020-11-02T18:10:55.877000+00:00",
                "last_login_at": "2020-11-02T18:10:55.877000+00:00",
                "identifier": "dedecu@hotmail.com",
                "id": "Ilq4ep1uzVYyRTGrmrYx",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:17:17.663364+00:00"
        },
        {
            "id": "huNekTffpByTzY3E7he5",
            "message": "appl.us not found, try again, please!",
            "sender": {
                "uid": "WhmylOoKgsT4zM8nKsJLTcnyA0v1",
                "created_at": "2020-11-02T22:34:55.684000+00:00",
                "last_login_at": "2020-11-02T22:34:55.684000+00:00",
                "identifier": "chatbot@chat.com",
                "id": "gv2wd0CevtWHSL6hpLpQ",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:17:18.974530+00:00"
        },
        {
            "id": "398ng3wWAfUUZ81IUOwq",
            "message": "",
            "sender": {
                "uid": "8IHMRHXQ1vOlRfnYE709G2vU3R12",
                "created_at": "2020-11-02T18:10:55.877000+00:00",
                "last_login_at": "2020-11-02T18:10:55.877000+00:00",
                "identifier": "dedecu@hotmail.com",
                "id": "Ilq4ep1uzVYyRTGrmrYx",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:17:25.716945+00:00"
        },
        {
            "id": "gvECIEDO2pMHeQhEEGz2",
            "message": "i will buy",
            "sender": {
                "uid": "8IHMRHXQ1vOlRfnYE709G2vU3R12",
                "created_at": "2020-11-02T18:10:55.877000+00:00",
                "last_login_at": "2020-11-02T18:10:55.877000+00:00",
                "identifier": "dedecu@hotmail.com",
                "id": "Ilq4ep1uzVYyRTGrmrYx",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:17:27.087250+00:00"
        },
        {
            "id": "FQSUxPjysyTHjeYOEzWo",
            "message": "/stock=aapl.us",
            "sender": {
                "uid": "oOaHPwczePZ8PuIRtnLHeUE3pcD3",
                "created_at": "2020-10-31T02:29:06.040000+00:00",
                "last_login_at": "2020-10-31T02:29:06.040000+00:00",
                "identifier": "dedeco@gmail.com",
                "id": "hJkqKYphnlt03e59AxVa",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:18:46.133836+00:00"
        },
        {
            "id": "IS4SRfjt4PeDZd25KMpC",
            "message": "aapl.us quote is $108.77 (close) per share",
            "sender": {
                "uid": "WhmylOoKgsT4zM8nKsJLTcnyA0v1",
                "created_at": "2020-11-02T22:34:55.684000+00:00",
                "last_login_at": "2020-11-02T22:34:55.684000+00:00",
                "identifier": "chatbot@chat.com",
                "id": "gv2wd0CevtWHSL6hpLpQ",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:18:47.547378+00:00"
        },
        {
            "id": "PGOjGhf5cvkifIqOZVqI",
            "message": "humm",
            "sender": {
                "uid": "8IHMRHXQ1vOlRfnYE709G2vU3R12",
                "created_at": "2020-11-02T18:10:55.877000+00:00",
                "last_login_at": "2020-11-02T18:10:55.877000+00:00",
                "identifier": "dedecu@hotmail.com",
                "id": "Ilq4ep1uzVYyRTGrmrYx",
                "provider": "password"
            },
            "created_at": "2020-11-02T23:18:56.958344+00:00"
        }
    ]
    }
   ```

## Chat bot 

 1. I have used the [huey](https://huey.readthedocs.io/en/latest/) as task queue lightweight alternative. 
 
 2. In other terminal after, run a redis locally:
 
     ``` 
    sudo docker run --name redis-chat -p 6379:6379 -d redis
    ```
3.  After the redis running on 0.0.0.0:6379->6379/tcp

    ``` 
    huey_consumer.py src.task.stock.huey
    ``` 
## Front end


 1. To run the frontend (requesit is setup a project on Firebase on GCP): 

    ``` 
     dev_appserver.py app.yaml
    ```  

  
