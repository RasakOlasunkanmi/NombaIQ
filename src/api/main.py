import hmac, hashlib, os
from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.post("/webhooks/nomba")
async def nomba_webhook(request: Request):
    body = await request.body()
    signature = request.headers.get("nomba-signature", "")
    expected = hmac.new(
        os.environ["NOMBA_WEBHOOK_SECRET"].encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected):
        raise HTTPException(status_code=401, detail="bad signature")

    event = await request.json()
    print("Webhook received:", event.get("type"))
    return {"status": "ok"}

# import hmac
# import hashlib
# import os
# from fastapi import FastAPI, Request, HTTPException
# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()

# engine = create_engine(os.environ["DATABASE_URL"])

# @app.post("/webhooks/nomba")
# async def nomba_webhook(request: Request):
#     body = await request.body()
#     signature = request.headers.get("nomba-signature", "")
    
#     expected = hmac.new(          # ← THIS is the bug: should be hmac.new()
#         os.environ["NOMBA_WEBHOOK_SECRET"].encode(),
#         body,
#         hashlib.sha256
#     ).hexdigest()

#     if not hmac.compare_digest(signature, expected):
#         raise HTTPException(status_code=401, detail="bad signature")

#     event = await request.json()
#     print("Webhook received:", event.get("type"))
#     return {"status": "ok"}