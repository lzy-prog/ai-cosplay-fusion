'use client'

import { useState } from 'react'
import { Download, RotateCcw, Eye, Sparkles } from 'lucide-react'

interface ResultDisplayProps {
  originalImage: string | null
  resultImage: string
  character: string
  onReset: () => void
}

export default function ResultDisplay({ 
  originalImage, 
  resultImage, 
  character, 
  onReset 
}: ResultDisplayProps) {
  const [activeTab, setActiveTab] = useState<'result' | 'original'>('result')
  const [isDownloading, setIsDownloading] = useState(false)

  const handleDownload = async () => {
    setIsDownloading(true)
    try {
      const response = await fetch(resultImage)
      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `cosplay-fusion-${character}-${Date.now()}.png`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (error) {
      console.error('下载失败:', error)
    } finally {
      setIsDownloading(false)
    }
  }

  return (
    <div className="card max-w-4xl mx-auto">
      <div className="text-center mb-6">
        <div className="flex items-center justify-center space-x-2 mb-2">
          <Sparkles className="h-6 w-6 text-purple-600" />
          <h2 className="text-2xl font-semibold text-gray-800">
            融合完成！
          </h2>
          <Sparkles className="h-6 w-6 text-purple-600" />
        </div>
        <p className="text-lg text-purple-600 font-medium">
          角色: {character}
        </p>
      </div>

      {/* 标签页 */}
      <div className="flex justify-center mb-6">
        <div className="bg-gray-100 rounded-lg p-1">
          <button
            onClick={() => setActiveTab('result')}
            className={`px-4 py-2 rounded-md font-medium transition-all duration-300 ${
              activeTab === 'result'
                ? 'bg-white text-purple-600 shadow-sm'
                : 'text-gray-600 hover:text-gray-800'
            }`}
          >
            <Eye className="h-4 w-4 inline mr-2" />
            融合结果
          </button>
          {originalImage && (
            <button
              onClick={() => setActiveTab('original')}
              className={`px-4 py-2 rounded-md font-medium transition-all duration-300 ${
                activeTab === 'original'
                  ? 'bg-white text-purple-600 shadow-sm'
                  : 'text-gray-600 hover:text-gray-800'
              }`}
            >
              <Eye className="h-4 w-4 inline mr-2" />
              原始图片
            </button>
          )}
        </div>
      </div>

      {/* 图片显示 */}
      <div className="mb-6">
        <div className="relative bg-gray-100 rounded-xl overflow-hidden">
          <img
            src={activeTab === 'result' ? resultImage : originalImage}
            alt={activeTab === 'result' ? '融合结果' : '原始图片'}
            className="w-full h-auto max-h-96 object-contain mx-auto"
          />
          
          {activeTab === 'result' && (
            <div className="absolute top-4 right-4">
              <div className="bg-white/90 backdrop-blur-sm rounded-lg px-3 py-2 text-sm font-medium text-gray-700">
                ✨ AI融合
              </div>
            </div>
          )}
        </div>
      </div>

      {/* 操作按钮 */}
      <div className="flex justify-center space-x-4">
        <button
          onClick={handleDownload}
          disabled={isDownloading}
          className="btn-primary flex items-center space-x-2"
        >
          <Download className="h-5 w-5" />
          <span>{isDownloading ? '下载中...' : '下载图片'}</span>
        </button>
        
        <button
          onClick={onReset}
          className="btn-secondary flex items-center space-x-2"
        >
          <RotateCcw className="h-5 w-5" />
          <span>重新开始</span>
        </button>
      </div>

      {/* 技术信息 */}
      <div className="mt-8 pt-6 border-t border-gray-200">
        <div className="text-center">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">
            处理详情
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
            <div className="bg-blue-50 rounded-lg p-4">
              <div className="text-blue-600 font-medium mb-1">角色识别</div>
              <div className="text-gray-600">AI自动识别角色: {character}</div>
            </div>
            <div className="bg-green-50 rounded-lg p-4">
              <div className="text-green-600 font-medium mb-1">背景生成</div>
              <div className="text-gray-600">Stable Diffusion生成专属背景</div>
            </div>
            <div className="bg-purple-50 rounded-lg p-4">
              <div className="text-purple-600 font-medium mb-1">智能融合</div>
              <div className="text-gray-600">光线和色彩自动匹配</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
