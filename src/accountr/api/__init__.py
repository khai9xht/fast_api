import sys
sys.path.append('./api')
sys.path.append('..')

from fastapi import APIRouter

import auth, operations, reports


router = APIRouter()
router.include_router(auth.router)
router.include_router(operations.router)
router.include_router(reports.router)
