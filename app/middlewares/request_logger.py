import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger

logger = get_logger()


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # correlation id (VERY useful in real systems)
        request_id = str(uuid.uuid4())

        # attach to request state
        request.state.request_id = request_id

        try:
            response = await call_next(request)

            process_time = (time.time() - start_time) * 1000

            log_message = (
                f"{request.method} {request.url.path} | "
                f"{int(process_time)}ms | "
                f"{response.status_code} | "
                f"request_id={request_id}"
            )

            if response.status_code >= 500:
                logger.error(log_message)
            elif response.status_code >= 400:
                logger.warning(log_message)
            else:
                logger.info(log_message)

            response.headers["X-Request-ID"] = request_id
            response.headers["X-Process-Time-ms"] = str(int(process_time))

            return response

        except Exception as e:
            process_time = (time.time() - start_time) * 1000

            logger.error(
                f"{request.method} {request.url.path} | "
                f"{int(process_time)}ms | ERROR | "
                f"request_id={request_id} | {str(e)}"
            )

            raise