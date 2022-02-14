"""prima migrazione

Revision ID: 03b15f0f9fec
Revises: 
Create Date: 2022-02-14 23:56:26.927059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b15f0f9fec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rioni',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rione', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('emailk', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('emailk'),
    sa.UniqueConstraint('username')
    )
    op.create_table('gare',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('numero_corsa', sa.Integer(), nullable=True),
    sa.Column('rione_id', sa.Integer(), nullable=False),
    sa.Column('valido', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['rione_id'], ['rioni.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=True),
    sa.Column('body', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('gare')
    op.drop_table('user')
    op.drop_table('rioni')
    # ### end Alembic commands ###