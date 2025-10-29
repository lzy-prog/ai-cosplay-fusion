'use client'

import { useState } from 'react'
import ImageUpload from '@/components/ImageUpload'
import ProcessingStatus from '@/components/ProcessingStatus'
import ResultDisplay from '@/components/ResultDisplay'
import Header from '@/components/Header'

export default function Home() {
  const [uploadedImage, setUploadedImage] = useState<string | null>(null)
  const [processingStatus, setProcessingStatus] = useState<string>('')
  const [isProcessing, setIsProcessing] = useState(false)
  const [resultImage, setResultImage] = useState<string | null>(null)
  const [recognizedCharacter, setRecognizedCharacter] = useState<string>('')

  const handleImageUpload = async (imageFile: File) => {
    setIsProcessing(true)
    setProcessingStatus('正在上传图片...')
    
    try {
      const formData = new FormData()
      formData.append('image', imageFile)
      
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'
      const response = await fetch(`${apiUrl}/api/process-image`, {
        method: 'POST',
        body: formData,
      })
      
      if (!response.ok) {
        throw new Error('处理失败')
      }
      
      const result = await response.json()
      setResultImage(result.resultImage)
      setRecognizedCharacter(result.character)
      setProcessingStatus('处理完成！')
    } catch (error) {
      console.error('处理错误:', error)
      setProcessingStatus('处理失败，请重试')
    } finally {
      setIsProcessing(false)
    }
  }

  const resetProcess = () => {
    setUploadedImage(null)
    setProcessingStatus('')
    setIsProcessing(false)
    setResultImage(null)
    setRecognizedCharacter('')
  }

  return (
    <main className="min-h-screen">
      <Header />
      
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-gray-800 mb-4">
              🎭 AI角色扮演场景融合器
            </h1>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              上传您的角色扮演照片，AI将自动识别角色并生成专属背景，创造完美的融合效果
            </p>
          </div>

          {!uploadedImage && !isProcessing && (
            <ImageUpload onImageUpload={handleImageUpload} />
          )}

          {isProcessing && (
            <ProcessingStatus 
              status={processingStatus}
              character={recognizedCharacter}
            />
          )}

          {resultImage && (
            <ResultDisplay 
              originalImage={uploadedImage}
              resultImage={resultImage}
              character={recognizedCharacter}
              onReset={resetProcess}
            />
          )}
        </div>
      </div>
    </main>
  )
}
