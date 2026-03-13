# MATLAB 在线/轻量化解决方案调研

本文档调研 MATLAB 的在线和轻量化替代方案。

---

## 一、在线 MATLAB 解决方案

### 1. MATLAB Online (官方)

- **网址**: https://matlab.mathworks.com
- **费用**: 需要 MATLAB 许可证
- **功能**: 完整 MATLAB 功能
- **优点**: 与本地 MATLAB 完全兼容
- **缺点**: 需要许可证，国内访问慢

### 2. MATLAB Drive

- **存储**: 5GB 免费在线存储
- **协作**: 支持文件同步

---

## 二、开源/免费替代方案

### 1. GNU Octave

| 特性 | 描述 |
|------|------|
| **兼容性** | 与 MATLAB 语法高度兼容 (约 95%) |
| **开源** | 完全免费 |
| **官网** | https://www.gnu.org/software/octave |

**在线版本**:
- **Octave Online**: https://octave-online.net (免费)
- **Binder + Octave**: https://mybinder.org/v2/gh/octave-online/octave-online-server/HEAD

### 2. Jupyter + Python

| 库 | 对应 MATLAB 功能 |
|----|-----------------|
| NumPy | 矩阵运算 |
| SciPy | 科学计算 |
| Matplotlib | 绘图 |
| Pandas | 数据分析 |
| Scikit-learn | 机器学习 |
| Statsmodels | 统计分析 |

### 3. SageMath

- **网址**: https://www.sagemath.org
- **特点**: 符号计算 + 数值计算
- **在线**: https://sagecell.sagemath.org (免费)

### 4. Maxima

- **用途**: 符号数学计算
- **官网**: https://maxima.sourceforge.io

---

## 三、云计算平台

### 1. Google Colab

```python
# 安装 Octave 内核
!apt install octave
%octave pkg install -forge signal
```

### 2. Azure Notebooks

- 免费 Jupyter notebooks
- 支持 R, Python, F#

### 3. Kaggle Notebooks

- 免费 GPU 使用
- 支持 MATLAB (通过 Octave)

---

## 四、API 型解决方案

### 1. MATLAB Compiler SDK

```matlab
% 编译为 Web 服务
compiler.build.standaloneApplication('myfunction.m')
```

### 2. MathWorks Cloud Center

- 部署 MATLAB 应用到云端
- 按使用付费

### 3. 第三方 API 服务

| 服务 | 功能 |
|------|------|
| **NumPy API** | Python NumPy 计算 |
| **SciPy API** | 科学计算 API |
| **Plotly** | 在线绘图 API |

---

## 五、方案对比

| 方案 | 成本 | 易用性 | MATLAB 兼容性 | 推荐度 |
|------|------|--------|---------------|--------|
| MATLAB Online | ¥ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Octave Online | 免费 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Python/Jupyter | 免费 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Colab | 免费 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| SageMath | 免费 | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

---

## 六、本项目采用方案

### 最终选择: Python (NumPy/SciPy) + 在线工具

**理由**:
1. 完全免费
2. 社区活跃
3. 资料丰富
4. 易于集成
5. 可通过 API 调用

### 替代映射表

| MATLAB 函数 | Python 实现 |
|------------|-------------|
| `fft()` | `numpy.fft()` |
| `filter()` | `scipy.signal.lfilter()` |
| `pca()` | `sklearn.decomposition.PCA` |
| `svd()` | `numpy.linalg.svd()` |
| `interp1()` | `scipy.interpolate.interp1d()` |
| `lsqnonneg()` | `scipy.optimize.nnls()` |
| `polyfit()` | `numpy.polyfit()` |
| `ode45()` | `scipy.integrate.odeint()` |
| `fft()` | `numpy.fft.fft()` |
| `corrcoef()` | `numpy.corrcoef()` |

---

## 七、快速开始

### 在线运行

1. **Octave Online**: https://octave-online.net
2. **Google Colab**: https://colab.research.google.com
3. **Kaggle**: https://www.kaggle.com/notebooks
4. **Binder**: https://mybinder.org

### 本地轻量化

```bash
# 安装 Python (推荐 Anaconda)
conda install numpy scipy matplotlib pandas scikit-learn

# 或安装 Octave
# Ubuntu
sudo apt install octave
# macOS
brew install octave
```

---

## 八、后续参考

- [MATLAB vs Python 对比](https://www.mathworks.com/matlabcentral/fileexchange/46829-matlab-python-numpy-equivalents)
- [Octave 语法兼容列表](https://octave.org/doc/v4.2.0/Compatibility-with-MATLAB.html)
- [NumPy 对照表](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)
