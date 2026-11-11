"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class LandingEntry(BaseModel):
    """落地批次明细结构。"""

    field_0: str | None = None  # 批次编号
    field_1: str | None = None  # 来源系统
    field_2: str | None = None  # 落地路径
    field_3: str | None = None  # 文件格式
    field_4: str | None = None  # 接收时间
    field_5: str | None = None  # 原始行数
    field_6: str | None = None  # 校验摘要
    field_7: str | None = None  # 字符编码

class OdslayerEntry(BaseModel):
    """贴源表明细结构。"""

    field_0: str | None = None  # 表编号
    field_1: str | None = None  # 源表名称
    field_2: str | None = None  # 目标表名
    field_3: str | None = None  # 同步模式
    field_4: str | None = None  # 分区字段
    field_5: str | None = None  # 保留天数
    field_6: str | None = None  # 字段映射
    field_7: str | None = None  # 增量水位

class DwdlayerEntry(BaseModel):
    """明细表明细结构。"""

    field_0: str | None = None  # 表编号
    field_1: str | None = None  # 业务域名称
    field_2: str | None = None  # 明细表名
    field_3: str | None = None  # 源表依赖
    field_4: str | None = None  # 清洗规则
    field_5: str | None = None  # 去重策略
    field_6: str | None = None  # 分区粒度
    field_7: str | None = None  # 刷新周期

class DwslayerEntry(BaseModel):
    """汇总表明细结构。"""

    field_0: str | None = None  # 表编号
    field_1: str | None = None  # 汇总主题
    field_2: str | None = None  # 聚合维度
    field_3: str | None = None  # 度量列定义
    field_4: str | None = None  # 上游明细表
    field_5: str | None = None  # 汇总粒度
    field_6: str | None = None  # 更新策略
    field_7: str | None = None  # 历史天数

class AdslayerEntry(BaseModel):
    """应用数据集明细结构。"""

    field_0: str | None = None  # 数据集编号
    field_1: str | None = None  # 业务应用名称
    field_2: str | None = None  # 输出表名
    field_3: str | None = None  # 查询模板
    field_4: str | None = None  # 下游消费方
    field_5: str | None = None  # 接口协议
    field_6: str | None = None  # 刷新策略
    field_7: str | None = None  # 版本号

class DatasourceEntry(BaseModel):
    """数据源连接明细结构。"""

    field_0: str | None = None  # 连接编号
    field_1: str | None = None  # 连接类型
    field_2: str | None = None  # 接入地址
    field_3: str | None = None  # 认证方式
    field_4: str | None = None  # 连接池配置
    field_5: str | None = None  # 超时秒数
    field_6: str | None = None  # 重试次数
    field_7: str | None = None  # 负责人

class PartitionEntry(BaseModel):
    """分区策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 分区字段
    field_3: str | None = None  # 分区粒度
    field_4: str | None = None  # 保留天数
    field_5: str | None = None  # 冷热阈值
    field_6: str | None = None  # 预建天数
    field_7: str | None = None  # 归档路径

class CleanseEntry(BaseModel):
    """清洗规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 输入表名
    field_2: str | None = None  # 目标表名
    field_3: str | None = None  # 空值处理
    field_4: str | None = None  # 格式校验
    field_5: str | None = None  # 异常阈值
    field_6: str | None = None  # 规则版本
    field_7: str | None = None  # 生效日期

class TransformEntry(BaseModel):
    """转换节点明细结构。"""

    field_0: str | None = None  # 节点编号
    field_1: str | None = None  # 输入表名
    field_2: str | None = None  # 输出表名
    field_3: str | None = None  # 转换表达式
    field_4: str | None = None  # 执行顺序
    field_5: str | None = None  # 依赖节点
    field_6: str | None = None  # 失败策略
    field_7: str | None = None  # 调度周期

class QualityEntry(BaseModel):
    """质量规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 校验表名
    field_2: str | None = None  # 目标字段
    field_3: str | None = None  # 校验表达式
    field_4: str | None = None  # 阈值下界
    field_5: str | None = None  # 阈值上界
    field_6: str | None = None  # 采样比例
    field_7: str | None = None  # 阻断级别

class LineageEntry(BaseModel):
    """血缘关系明细结构。"""

    field_0: str | None = None  # 关系编号
    field_1: str | None = None  # 上游表名
    field_2: str | None = None  # 下游表名
    field_3: str | None = None  # 来源字段
    field_4: str | None = None  # 目标字段
    field_5: str | None = None  # 转换函数
    field_6: str | None = None  # 采集批次
    field_7: str | None = None  # 关系版本

class BackfillEntry(BaseModel):
    """补数任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 开始日期
    field_3: str | None = None  # 结束日期
    field_4: str | None = None  # 并行度
    field_5: str | None = None  # 覆盖策略
    field_6: str | None = None  # 完成水位
    field_7: str | None = None  # 失败区间

class SchemaEntry(BaseModel):
    """字段定义明细结构。"""

    field_0: str | None = None  # 字段编号
    field_1: str | None = None  # 所属表名
    field_2: str | None = None  # 字段名称
    field_3: str | None = None  # 字段类型
    field_4: str | None = None  # 可空标识
    field_5: str | None = None  # 默认值
    field_6: str | None = None  # 业务含义
    field_7: str | None = None  # 版本号

class DatasyncEntry(BaseModel):
    """同步链路明细结构。"""

    field_0: str | None = None  # 链路编号
    field_1: str | None = None  # 源端连接
    field_2: str | None = None  # 目标端连接
    field_3: str | None = None  # 同步表列表
    field_4: str | None = None  # 全量增量标识
    field_5: str | None = None  # 同步频率
    field_6: str | None = None  # 延迟阈值
    field_7: str | None = None  # 告警接收人

class SnapshotEntry(BaseModel):
    """快照策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 快照周期
    field_3: str | None = None  # 保留份数
    field_4: str | None = None  # 存储介质
    field_5: str | None = None  # 压缩格式
    field_6: str | None = None  # 过期清理
    field_7: str | None = None  # 恢复测试

class GovernEntry(BaseModel):
    """治理策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 治理类型
    field_3: str | None = None  # 冷热判定字段
    field_4: str | None = None  # 生命周期天数
    field_5: str | None = None  # 归档目标
    field_6: str | None = None  # 回收站保留
    field_7: str | None = None  # 执行频率

class MonitorEntry(BaseModel):
    """监控配置明细结构。"""

    field_0: str | None = None  # 配置编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 监控指标
    field_3: str | None = None  # 告警阈值
    field_4: str | None = None  # 告警级别
    field_5: str | None = None  # 静默分钟
    field_6: str | None = None  # 通知渠道
    field_7: str | None = None  # 恢复条件

class AuditEntry(BaseModel):
    """审计记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 操作表名
    field_2: str | None = None  # 变更类型
    field_3: str | None = None  # 变更前值
    field_4: str | None = None  # 变更后值
    field_5: str | None = None  # 操作时间
    field_6: str | None = None  # 操作来源
    field_7: str | None = None  # 回滚脚本
