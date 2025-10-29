'use client'

import { useCallback, useState } from 'react'
import { useDropzone } from 'react-dropzone'
import { Upload, Image as ImageIcon, AlertCircle } from 'lucide-react'

interface ImageUploadProps {
  onImageUpload: (file: File) => void
}

export default function ImageUpload({ onImageUpload }: ImageUploadProps) {
  const [preview, setPreview] = useState<string | null>(null)
  const [error, setError] = useState<string>('')

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0]
    
    if (!file) return
    
    // 验证文件类型
    if (!file.type.startsWith('image/')) {
      setError('请上传图片文件')
      return
    }
    
    // 验证文件大小 (最大10MB)
    if (file.size > 10 * 1024 * 1024) {
      setError('图片大小不能超过10MB')
      return
    }
    
    setError('')
    
    // 创建预览
    const reader = new FileReader()
    reader.onload = () => {
      setPreview(reader.result as string)
    }
    reader.readAsDataURL(file)
    
    // 上传文件
    onImageUpload(file)
  }, [onImageUpload])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.webp']
    },
    multiple: false
  })

  return (
    <div className="card max-w-2xl mx-auto">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-semibold text-gray-800 mb-2">
          上传您的角色扮演照片
        </h2>
        <p className="text-gray-600">
          支持 JPG、PNG 格式，最大 10MB
        </p>
      </div>

      {error && (
        <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-center space-x-2 text-red-700">
          <AlertCircle className="h-5 w-5" />
          <span>{error}</span>
        </div>
      )}

      <div
        {...getRootProps()}
        className={`
          border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-300
          ${isDragActive 
            ? 'border-purple-500 bg-purple-50' 
            : 'border-gray-300 hover:border-purple-400 hover:bg-gray-50'
          }
        `}
      >
        <input {...getInputProps()} />
        
        {preview ? (
          <div className="space-y-4">
            <div className="relative inline-block">
              <img
                src={preview}
                alt="预览"
                className="max-h-64 rounded-lg shadow-md"
              />
            </div>
            <p className="text-sm text-gray-600">
              点击或拖拽更换图片
            </p>
          </div>
        ) : (
          <div className="space-y-4">
            <div className="flex justify-center">
              {isDragActive ? (
                <Upload className="h-16 w-16 text-purple-500" />
              ) : (
                <ImageIcon className="h-16 w-16 text-gray-400" />
              )}
            </div>
            
            <div>
              <p className="text-lg font-medium text-gray-700 mb-2">
                {isDragActive ? '释放文件开始上传' : '拖拽图片到此处'}
              </p>
              <p className="text-gray-500 mb-4">
                或者点击选择文件
              </p>
              <button className="btn-primary">
                选择图片
              </button>
            </div>
          </div>
        )}
      </div>

      <div className="mt-6 text-center">
        <div className="flex justify-center space-x-6 text-sm text-gray-500">
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <span>自动识别角色</span>
          </div>
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
            <span>生成专属背景</span>
          </div>
          <div className="flex items-center space-x-1">
            <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
            <span>智能融合处理</span>
          </div>
        </div>
      </div>
    </div>
  )
}
