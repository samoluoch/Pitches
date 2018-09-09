"""modified r/ship in User table

Revision ID: 822df7281ad5
Revises: 702999186536
Create Date: 2018-09-09 11:21:49.150537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '822df7281ad5'
down_revision = '702999186536'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_pitch_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'pitch_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_pitch_id_fkey', 'users', 'pitch', ['pitch_id'], ['id'])
    # ### end Alembic commands ###