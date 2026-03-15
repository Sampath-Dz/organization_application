from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(".."))
from models.db_base import Base
import models.models

# Alembic Config object
config = context.config

# Logging setup
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate
target_metadata = Base.metadata

from settings import DATABASE_URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ----------------------
# Include object filter
# ----------------------
def include_object(object, name, type_, reflected, compare_to):
    allowed_tables = ["organizations", "teams", "members"]  # only core_service tables
    if type_ == "table" and name not in allowed_tables:
        return False  # ignore other tables
    return True

# ----------------------
# Offline migrations
# ----------------------
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,  # apply filter here too
    )

    with context.begin_transaction():
        context.run_migrations()

# ----------------------
# Online migrations
# ----------------------
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,  # <-- filter applied here
        )

        with context.begin_transaction():
            context.run_migrations()

# ----------------------
# Run appropriate mode
# ----------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
