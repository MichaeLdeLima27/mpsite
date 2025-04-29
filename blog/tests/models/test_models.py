from django.contrib.auth.models import User
from blog.models import Post
import pytest

@pytest.mark.django_db
def test_criacao_post():
    # Criando um usuário para associar ao post
    user = User.objects.create_user(username="michael", password="senha123")

    # Criando o post
    post = Post.objects.create(
        title="Post de Teste",
        content="Conteúdo do post de teste.",
        author=user  # Aqui você passa a instância do usuário
    )

    # Verificando se o post foi criado com sucesso
    assert post.title == "Post de Teste"
    assert post.content == "Conteúdo do post de teste."
    assert post.author == user
