"""
Contains schemas to api
"""

from pydantic import BaseModel


class GameCard(BaseModel):
    """
    Schema to request json
    """
    id: str
    title: str
    namespace: str
    description: str
    effectiveDate: str
    offerType: str
    expiryDate: None
    status: str
    isCodeRedemptionOnly: bool
    keyImages: list[dict]
    seller: dict
    productSlug: str
    urlSlug: str
    url: None
    items: list[dict]
    customAttributes: list[dict]
    categories: list[dict]
    tags: list[dict]
    catalogNs: dict
    offerMappings: list
    price: dict
    promotions: None
