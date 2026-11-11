import { useState } from 'react'
import { Link, Route, Routes } from 'react-router-dom'

import Overview from './views/Overview'
import LandingView from './views/landing'
import OdslayerView from './views/odslayer'
import DwdlayerView from './views/dwdlayer'
import DwslayerView from './views/dwslayer'
import AdslayerView from './views/adslayer'
import DatasourceView from './views/datasource'
import PartitionView from './views/partition'
import CleanseView from './views/cleanse'
import TransformView from './views/transform'
import QualityView from './views/quality'
import LineageView from './views/lineage'
import BackfillView from './views/backfill'
import SchemaView from './views/schema'
import DatasyncView from './views/datasync'
import SnapshotView from './views/snapshot'
import GovernView from './views/govern'
import MonitorView from './views/monitor'
import AuditView from './views/audit'

const navItems = [{ label: "运营概览", path: "/" }, { label: "原始落地", path: "/landing" }, { label: "贴源层建模", path: "/odslayer" }, { label: "明细层建模", path: "/dwdlayer" }, { label: "汇总层建模", path: "/dwslayer" }, { label: "应用层发布", path: "/adslayer" }, { label: "数据源管理", path: "/datasource" }, { label: "分区治理", path: "/partition" }, { label: "清洗加工", path: "/cleanse" }, { label: "转换编排", path: "/transform" }, { label: "质量校验", path: "/quality" }, { label: "血缘追踪", path: "/lineage" }, { label: "历史补数", path: "/backfill" }, { label: "元数据管理", path: "/schema" }, { label: "数据同步", path: "/datasync" }, { label: "快照管理", path: "/snapshot" }, { label: "存储治理", path: "/govern" }, { label: "任务监控", path: "/monitor" }, { label: "变更审计", path: "/audit" }]

export default function App() {
  const [operator] = useState('值班管理员')

  return (
    <div className="app-shell">
      <aside className="app-side">
        <h1 className="app-title">分层数据仓库治理平台</h1>
        <nav className="nav-list">
          {navItems.map((item) => (
            <Link key={item.path} to={item.path} className="nav-item">
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="app-main">
        <header className="app-head">
          <span className="head-desc">面向原始数据落地、分层清洗建模、分区治理、质量校验、血缘追踪与历史补数的分层数据仓库治理平台。</span>
          <span className="head-user">当前值班：{operator}</span>
        </header>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/landing" element={<LandingView />} />
          <Route path="/odslayer" element={<OdslayerView />} />
          <Route path="/dwdlayer" element={<DwdlayerView />} />
          <Route path="/dwslayer" element={<DwslayerView />} />
          <Route path="/adslayer" element={<AdslayerView />} />
          <Route path="/datasource" element={<DatasourceView />} />
          <Route path="/partition" element={<PartitionView />} />
          <Route path="/cleanse" element={<CleanseView />} />
          <Route path="/transform" element={<TransformView />} />
          <Route path="/quality" element={<QualityView />} />
          <Route path="/lineage" element={<LineageView />} />
          <Route path="/backfill" element={<BackfillView />} />
          <Route path="/schema" element={<SchemaView />} />
          <Route path="/datasync" element={<DatasyncView />} />
          <Route path="/snapshot" element={<SnapshotView />} />
          <Route path="/govern" element={<GovernView />} />
          <Route path="/monitor" element={<MonitorView />} />
          <Route path="/audit" element={<AuditView />} />
        </Routes>
      </main>
    </div>
  )
}
