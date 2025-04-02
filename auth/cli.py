from argparse import _SubParsersAction

from pydantic import validate_email
from pydantic_core import PydanticCustomError
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.db import engine
from auth.models import create_user, get_user_by_email
from auth.schemas import UserCreate

FAIL = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

async def create_user_from_cli(args):
    print(args)
    email_is_valid = False
    email_checked = False
    email = args.email
    while not email_is_valid and not email_checked:
        try:
            email_parts = validate_email(email)
            print("email_parts", email_parts)
            email_is_valid = True
            email=email_parts[1]
        except PydanticCustomError:
            email = input("Enter a valid email: ")

        async with AsyncSession(engine) as session:
            if await get_user_by_email(session=session, email=email):
                print(FAIL + "User with this email already exists" + ENDC)
                email_is_valid = False
            else:
                email_checked = True

    if args.password is None:
        password = input("Enter password: ")
    else:
        password = args.password

    user = UserCreate(email=email, password=password)
    user.is_superuser = args.command == "createsuperuser"

    async with AsyncSession(engine) as session:
        await create_user(session=session, user_create=user)

    print(OKGREEN + 'User created' + ENDC)


def register_commands(subparsers: _SubParsersAction):
    parser = subparsers.add_parser(
        'createuser',
        help="Create regular user"
    )
    parser.set_defaults(func=create_user_from_cli)
    parser.add_argument(
        '--email', '-e',
        help='user Email',
        type=str, default='not_valid_email'
    )
    parser.add_argument(
        "--password", '-p',
        help='user password',
        type=str, default=None
    )


    parser = subparsers.add_parser(
        'createsuperuser',
        help="Create super user"
    )
    parser.set_defaults(func=create_user_from_cli)
    parser.add_argument(
        '--email', '-e',
        help='user Email',
        type=str, default='not_valid_email'
    )
    parser.add_argument(
        "--password", '-p',
        help='user password',
        type=str, default=None
    )    
