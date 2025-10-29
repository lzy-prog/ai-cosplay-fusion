'use client'

import { Sparkles, Camera, Palette } from 'lucide-react'

export default function Header() {
  return (
    <header className="bg-white/80 backdrop-blur-sm border-b border-gray-200 sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <Sparkles className="h-8 w-8 text-purple-600" />
              <h1 className="text-2xl font-bold text-gray-800">
                AI Cosplay Fusion
              </h1>
            </div>
          </div>
          
          <div className="flex items-center space-x-6 text-sm text-gray-600">
            <div className="flex items-center space-x-2">
              <Camera className="h-4 w-4" />
              <span>智能识别</span>
            </div>
            <div className="flex items-center space-x-2">
              <Palette className="h-4 w-4" />
              <span>背景生成</span>
            </div>
            <div className="flex items-center space-x-2">
              <Sparkles className="h-4 w-4" />
              <span>完美融合</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}
