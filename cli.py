import asyncio
import inspect
from app.core.cli import parser


if __name__ == "__main__":
    args = parser.parse_args()
    if inspect.iscoroutinefunction(args.func):
        asyncio.run(args.func(args))
    else:
        args.func(args)
