"""empty message

Revision ID: 50f6fd0283a5
Revises: 10377eb2d235
Create Date: 2024-08-12 10:25:30.890020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f6fd0283a5'
down_revision = '10377eb2d235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ids_rules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rule', sa.Text(), nullable=False),
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('rev', sa.Integer(), nullable=True),
    sa.Column('msg', sa.Text(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True, default=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ids_rules')
    # ### end Alembic commands ###
