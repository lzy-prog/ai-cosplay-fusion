'use client'

import { useEffect, useState } from 'react'
import { Loader2, Eye, Palette, Zap } from 'lucide-react'

interface ProcessingStatusProps {
  status: string
  character?: string
}

const processingSteps = [
  { id: 'upload', label: '上传图片', icon: '📤' },
  { id: 'recognize', label: '识别角色', icon: '🔍' },
  { id: 'generate', label: '生成背景', icon: '🎨' },
  { id: 'extract', label: '抠图处理', icon: '✂️' },
  { id: 'blend', label: '融合合成', icon: '✨' },
  { id: 'complete', label: '处理完成', icon: '🎉' }
]

export default function ProcessingStatus({ status, character }: ProcessingStatusProps) {
  const [currentStep, setCurrentStep] = useState(0)
  const [progress, setProgress] = useState(0)

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(interval)
          return 100
        }
        return prev + Math.random() * 10
      })
    }, 500)

    return () => clearInterval(interval)
  }, [])

  useEffect(() => {
    if (status.includes('上传')) setCurrentStep(0)
    else if (status.includes('识别')) setCurrentStep(1)
    else if (status.includes('生成')) setCurrentStep(2)
    else if (status.includes('抠图')) setCurrentStep(3)
    else if (status.includes('融合')) setCurrentStep(4)
    else if (status.includes('完成')) setCurrentStep(5)
  }, [status])

  return (
    <div className="card max-w-2xl mx-auto">
      <div className="text-center mb-8">
        <div className="flex justify-center mb-4">
          <div className="relative">
            <Loader2 className="h-16 w-16 text-purple-600 animate-spin" />
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="h-8 w-8 bg-white rounded-full flex items-center justify-center">
                <span className="text-lg">{processingSteps[currentStep]?.icon}</span>
              </div>
            </div>
          </div>
        </div>
        
        <h2 className="text-2xl font-semibold text-gray-800 mb-2">
          {status}
        </h2>
        
        {character && (
          <p className="text-lg text-purple-600 font-medium">
            识别到角色: {character}
          </p>
        )}
      </div>

      {/* 进度条 */}
      <div className="mb-8">
        <div className="flex justify-between text-sm text-gray-600 mb-2">
          <span>处理进度</span>
          <span>{Math.round(progress)}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div 
            className="bg-gradient-to-r from-purple-500 to-blue-500 h-3 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${progress}%` }}
          ></div>
        </div>
      </div>

      {/* 处理步骤 */}
      <div className="space-y-4">
        {processingSteps.map((step, index) => (
          <div 
            key={step.id}
            className={`flex items-center space-x-4 p-3 rounded-lg transition-all duration-300 ${
              index <= currentStep 
                ? 'bg-purple-50 border border-purple-200' 
                : 'bg-gray-50 border border-gray-200'
            }`}
          >
            <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
              index < currentStep 
                ? 'bg-green-500 text-white' 
                : index === currentStep 
                ? 'bg-purple-500 text-white animate-pulse' 
                : 'bg-gray-300 text-gray-600'
            }`}>
              {index < currentStep ? '✓' : index + 1}
            </div>
            
            <div className="flex-1">
              <div className="flex items-center space-x-2">
                <span className="text-lg">{step.icon}</span>
                <span className={`font-medium ${
                  index <= currentStep ? 'text-gray-800' : 'text-gray-500'
                }`}>
                  {step.label}
                </span>
              </div>
              
              {index === currentStep && (
                <div className="mt-1">
                  <div className="flex items-center space-x-2 text-sm text-purple-600">
                    <Loader2 className="h-3 w-3 animate-spin" />
                    <span>处理中...</span>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8 text-center text-sm text-gray-500">
        <p>AI正在为您精心处理，请稍候...</p>
        <p className="mt-1">预计还需要 30-60 秒</p>
      </div>
    </div>
  )
}
