from typing import Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    Módulo: product_model

    Este módulo define o modelo de dados `Product` utilizando Pydantic para validação e documentação de produtos.

    Classes:
        Product (BaseModel): Representa um produto com informações detalhadas sobre tipo, marcas, variação, embalagem, quantidade e unidade de medida.

    Atributos da classe Product:
        type (str): Tipo do produto.
        primary_brand (str): Marca principal do produto.
        secondary_brand (Optional[str]): Marca secundária do produto, se houver.
        variation (Optional[str]): Variação do produto, como sabor, cor, etc.
        container (Optional[str]): Embalagem do produto.
        container_type (Optional[str]): Material da embalagem do produto.
        amount (Optional[int]): Quantidade de produtos, padrão é 1.
        measure (Optional[int] | Optional[float]): Medida do produto (peso, volume, etc).
        unity (Optional[str]): Unidade de medida do produto.

    Exemplo de uso:
        product = Product(
            type="Bebida",
            primary_brand="MarcaX",
            secondary_brand="MarcaY",
            variation="Limão",
            container="Garrafa",
            container_type="Plástico",
            amount=6,
            measure=500,
            unity="ml"
    """
    type: str = Field(description="Product type")
    primary_brand: str = Field(description="Primary brand of the product")
    secondary_brand: Optional[str] = Field(
        description="Secondary brand of the product", default=None
    )
    variation: Optional[str] = Field(
        description="Variation of the product, such as flavor, etc", default=None
    )
    container: Optional[str] = Field(description="The product container", default=None)
    container_type: Optional[str] = Field(description="The container material", default=None)
    amount: Optional[int] = Field(description="Amount of products if any", default=1)
    measure: Optional[int] | Optional[float] = Field(
        description="Measurement of the product", default=None
    )
    unity: Optional[str] = Field(
        description="The unity of measurement of the product", default=None
    )
