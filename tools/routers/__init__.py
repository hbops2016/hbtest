from fastapi import APIRouter, Depends

import deps
from .tools_router import router as tools
tool_router = APIRouter()

# api_router.include_router(project, prefix="/project", tags=["project"], dependencies=[Depends(deps.get_current_active_user)])
# api_router.include_router(environment, prefix="/environment", tags=["environment"],dependencies=[Depends(deps.get_current_active_user)])

tool_router.include_router(tools, prefix="/tools", tags=["tools"])
