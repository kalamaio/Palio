"""aggiornamento

Revision ID: 6b3b557a9f44
Revises: 622dcd1638ee
Create Date: 2022-04-05 12:58:34.902467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3b557a9f44'
down_revision = '622dcd1638ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gare', schema=None) as batch_op:
        batch_op.add_column(sa.Column('immagine', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('gare', schema=None) as batch_op:
        batch_op.drop_column('immagine')

    # ### end Alembic commands ###
