# SVD Image Compression

Connecting **Linear Algebra, Image Processing, and Machine Learning**.

---

## Overview

Singular Value Decomposition (SVD) is a linear algebra technique that decomposes a matrix into orthogonal components. Applied to images, it allows **compression, reconstruction, and pattern discovery**.

An image represented as a matrix \(A\) can be factorized as:

$$
A = U \Sigma V^T
$$

Where:

- \(U\) = orthogonal matrix (left singular vectors)  
- \(\Sigma\) = diagonal matrix of singular values  
- \(V^T\) = orthogonal matrix (right singular vectors)  
- \(\sigma_i\) = singular values capturing the energy in the image

---

## Image Reconstruction

Reconstruction using top-\(k\) components:

$$
A \approx \sum_{i=1}^{k} \sigma_i u_i v_i^T
$$

Cumulative energy captured by first \(k\) singular values:

$$
E(k) = \frac{\sum_{i=1}^{k} \sigma_i^2}{\sum_{i=1}^{r} \sigma_i^2}
$$

Where \(r\) = rank of the image.  
Most of the information is concentrated in the **first few singular values**.

---

## Key Insights

- With ~50 components, the reconstructed image looks almost identical to the original while **reducing file size drastically**  
- Error vs. \(k\) shows the **trade-off between compression and accuracy**  
- Each singular component reveals **hidden patterns** that together reconstruct the full image  

---

## Relevance to Machine Learning

- **PCA (Principal Component Analysis)** uses SVD for dimensionality reduction  
- SVD is also used for **feature extraction, noise reduction, and latent factor models**  
- Linear algebra forms the foundation of **many ML algorithms**  

---

## Usage

1. Place your images in the `images/` folder  
2. Open `SVD_Image_Compression.ipynb`  
3. Run all cells to generate:
   - Original and reconstructed images  
   - Singular value plots  
   - Cumulative energy and error plots  

---

## Dependencies

- Python 3.x  
- `numpy`, `matplotlib`, `seaborn`, `Pillow`  

Install dependencies:

```bash
pip install numpy matplotlib seaborn Pillow
