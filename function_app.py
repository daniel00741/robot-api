import azure.functions as func

from src.main import fastapi_app


app = func.AsgiFunctionApp(
    app=fastapi_app,
    http_auth_level=func.AuthLevel.ANONYMOUS
)
# import json
# import logging

# import azure.functions as func

# app = func.FunctionApp()


# @app.route(
#     route="health_check",
#     methods=["GET"],
#     auth_level=func.AuthLevel.ANONYMOUS
# )
# def health_check(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info("Health check requested.")

#     response = {
#         "status": "ok",
#         "service": "robot-api",
#         "environment": "dev",
#         "message": "Robot API is running"
#     }

#     return func.HttpResponse(
#         body=json.dumps(response),
#         status_code=200,
#         mimetype="application/json"
#     )
#####################################################333
# import azure.functions as func
# import datetime
# import json
# import logging

# app = func.FunctionApp()

# @app.route(route="health_check", auth_level=func.AuthLevel.ANONYMOUS)
# def health_check(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )