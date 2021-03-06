"""added many to many relationship on trips and riders models

Revision ID: 25476460139b
Revises: 1383fc82fb0b
Create Date: 2019-05-29 03:00:57.399354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25476460139b'
down_revision = '1383fc82fb0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('riders',
    sa.Column('rider_id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rider_id'], ['rider.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('rider_id', 'trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('riders')
    # ### end Alembic commands ###
