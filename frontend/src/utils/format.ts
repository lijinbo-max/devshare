export const formatDate = (dateString: string): string => {
  const date = new Date(dateString)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

export const formatRelativeTime = (dateString: string): string => {
  const date = new Date(dateString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))

  if (days === 0) return '今天'
  if (days === 1) return '昨天'
  if (days < 7) return `${days}天前`
  if (days < 30) return `${Math.floor(days / 7)}周前`
  if (days < 365) return `${Math.floor(days / 30)}个月前`
  return `${Math.floor(days / 365)}年前`
}

export const truncateText = (text: string, maxLength: number): string => {
  if (text.length <= maxLength) return text
  return text.substring(0, maxLength) + '...'
}

export const highlightCode = (code: string, language: string): string => {
  const keywords: Record<string, string[]> = {
    python: ['def', 'return', 'if', 'else', 'elif', 'for', 'while', 'import', 'from', 'class', 'self', 'True', 'False', 'None', 'and', 'or', 'not'],
    javascript: ['function', 'return', 'if', 'else', 'for', 'while', 'const', 'let', 'var', 'class', 'import', 'export', 'from', 'async', 'await', 'true', 'false', 'null', 'undefined'],
    typescript: ['function', 'return', 'if', 'else', 'for', 'while', 'const', 'let', 'var', 'class', 'import', 'export', 'from', 'async', 'await', 'true', 'false', 'null', 'undefined', 'interface', 'type', 'extends', 'implements'],
    rust: ['fn', 'return', 'if', 'else', 'for', 'while', 'let', 'mut', 'const', 'struct', 'enum', 'impl', 'pub', 'use', 'mod', 'crate', 'self', 'true', 'false'],
    java: ['public', 'private', 'protected', 'static', 'void', 'return', 'if', 'else', 'for', 'while', 'class', 'interface', 'extends', 'implements', 'import', 'package', 'new', 'null', 'true', 'false']
  }

  const langKeywords = keywords[language.toLowerCase()] || []
  let highlighted = code
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')

  langKeywords.forEach(keyword => {
    const regex = new RegExp(`\\b(${keyword})\\b`, 'g')
    highlighted = highlighted.replace(regex, '<span class="keyword">$1</span>')
  })

  highlighted = highlighted.replace(/(['"`])(.*?)\1/g, '<span class="string">$1$2$1</span>')
  highlighted = highlighted.replace(/(\/\/.*$)/gm, '<span class="comment">$1</span>')
  highlighted = highlighted.replace(/(#.*$)/gm, '<span class="comment">$1</span>')
  highlighted = highlighted.replace(/(\d+)/g, '<span class="number">$1</span>')

  return highlighted
}

export const generateSlug = (title: string): string => {
  return title
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9\u4e00-\u9fa5]+/g, '-')
    .replace(/^-|-$/g, '')
}
