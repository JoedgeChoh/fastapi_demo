#! /usr/bin/env python3

from fastapi import APIRouter

router = APIRouter(
        prefix = '/add',
        tags = ['addition']
        )

@router.get('/numbers')
async def add_numbers():
    return {"message": "we are adding numbers"}

@router.get('/strings')
async def add_strings():
    return {"message": "we are adding strings"}
