"""empty message

Revision ID: 1383fc82fb0b
Revises: 72aaafb62814
Create Date: 2019-05-10 03:08:05.315934

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1383fc82fb0b'
down_revision = '72aaafb62814'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trip', sa.Column('departure_date', sa.DateTime(timezone=True), nullable=False))
    op.add_column('trip', sa.Column('driver_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'trip', 'driver', ['driver_id'], ['id'])
    op.drop_column('trip', 'depature_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trip', sa.Column('depature_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'trip', type_='foreignkey')
    op.drop_column('trip', 'driver_id')
    op.drop_column('trip', 'departure_date')
    # ### end Alembic commands ###