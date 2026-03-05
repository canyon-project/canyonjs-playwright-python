# 发布步骤

## 1. 更新版本号

编辑 `pyproject.toml`，修改 `version` 字段：

```toml
[project]
name = "canyonjs-playwright"
version = "0.1.1"  # 改为新版本号，如 0.1.1、1.0.0
```

## 2. 提交并推送

```bash
git add pyproject.toml
git commit -m "chore: bump version to x.x.x"
git push origin main
```

## 3. 创建 GitHub Release

1. 打开仓库的 **Releases** 页面：`https://github.com/<org>/canyonjs-playwright-python/releases`
2. 点击 **Create a new release**
3. 填写：
   - **Choose a tag**：输入新 tag，如 `v0.1.1`（建议与版本号一致，加 `v` 前缀）
   - **Release title**：如 `v0.1.1` 或简短说明
   - **Description**：本次更新的变更说明（可选）
4. 点击 **Publish release**

## 4. 自动发布到 PyPI

发布 Release 后，GitHub Actions 会自动运行 `publish.yml` 工作流，构建并上传到 PyPI。

- 查看运行状态：仓库 **Actions** 标签页
- 发布成功后，用户可通过 `pip install canyonjs-playwright` 安装新版本
