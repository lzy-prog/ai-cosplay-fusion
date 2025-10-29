import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'AI角色扮演场景融合器',
  description: '通过AI识别角色并生成背景进行图像融合的专业工具',
  keywords: ['AI', '角色扮演', '图像融合', '背景生成', 'Cosplay'],
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh-CN">
      <body className={inter.className}>
        <div className="min-h-screen">
          {children}
        </div>
      </body>
    </html>
  )
}
