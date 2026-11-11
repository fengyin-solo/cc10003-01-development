"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import landing as router_landing
from app.routers import odslayer as router_odslayer
from app.routers import dwdlayer as router_dwdlayer
from app.routers import dwslayer as router_dwslayer
from app.routers import adslayer as router_adslayer
from app.routers import datasource as router_datasource
from app.routers import partition as router_partition
from app.routers import cleanse as router_cleanse
from app.routers import transform as router_transform
from app.routers import quality as router_quality
from app.routers import lineage as router_lineage
from app.routers import backfill as router_backfill
from app.routers import schema as router_schema
from app.routers import datasync as router_datasync
from app.routers import snapshot as router_snapshot
from app.routers import govern as router_govern
from app.routers import monitor as router_monitor
from app.routers import audit as router_audit

ROUTERS = [router_landing, router_odslayer, router_dwdlayer, router_dwslayer, router_adslayer, router_datasource, router_partition, router_cleanse, router_transform, router_quality, router_lineage, router_backfill, router_schema, router_datasync, router_snapshot, router_govern, router_monitor, router_audit]
